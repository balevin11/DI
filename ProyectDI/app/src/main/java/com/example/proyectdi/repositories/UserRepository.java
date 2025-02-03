package com.example.proyectdi.repositories;

import com.example.proyectdi.models.User;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.*;

public class UserRepository {
    private FirebaseAuth mAuth;
    //constructor
    public UserRepository() {
    }

    // Interfaz para devolver el resultado del registro
    public interface RegistrationCallback {
        void onSuccess();
        void onFailure(String errorMessage);
    }



    public void setUser(String email, String password, String fullName, String address, int phone, RegistrationCallback callback){//crear un nuevo usuario en firebase con gmail y contraseña, toast de error y éxito
        // Inicializa FirebaseAuth para el manejo de autenticación
        mAuth = FirebaseAuth.getInstance();
        //crear un nuevo usuario con email y contraseña
        mAuth.createUserWithEmailAndPassword(email, password).addOnCompleteListener(task -> {
            if (task.isSuccessful()) {

                // Si la creación fue exitosa, obtener el usuario registrado
                FirebaseUser firebaseUser = mAuth.getCurrentUser();
                if (firebaseUser != null) {
                    String uid = firebaseUser.getUid(); // Obtener el ID del usuario

                    // Crear un objeto con los datos adicionales
                    User newUser = new User(uid, fullName, email, address, phone);
                    DatabaseReference databaseRef = FirebaseDatabase
                            .getInstance("https://proyecto-di-26dcb-default-rtdb.europe-west1.firebasedatabase.app/")
                            .getReference("users");

                    // Guardar los datos del usuario en la base de datos bajo el UID
                    databaseRef.child(uid).setValue(newUser)
                            .addOnCompleteListener(dbTask -> {
                                if (dbTask.isSuccessful()) {
                                    callback.onSuccess();  // Registro exitoso
                                } else {
                                    callback.onFailure("Error al guardar los datos del usuario.");
                                }
                            });
                }
            } else {
                Exception exception = task.getException(); if (exception != null) {
                    String errorMessage = exception.getMessage();  // Obtener el mensaje de la excepción
                    callback.onFailure(errorMessage);
                } else {
                    // Si no hay un error específico, muestra un mensaje genérico
                    callback.onFailure("Error desconocido en el registro.");
                }
            }
        });
    }
    // Interfaz para devolver el resultado del login
    public interface LoginCallback {
        void onSuccess();
        void onFailure(String errorMessage);
    }

    public void LoginUser(String email, String password, LoginCallback callback ){
        // Inicializa FirebaseAuth para el manejo de autenticación
        mAuth = FirebaseAuth.getInstance();
        //iniciar sesion en firebase con email y contraseña, toast de error y éxito
        mAuth.signInWithEmailAndPassword(email, password).addOnCompleteListener(task -> {
            if (task.isSuccessful()) {
                 callback.onSuccess();
            } else {
                callback.onFailure("Error en autenticación.");
            }
        });
    }
}
