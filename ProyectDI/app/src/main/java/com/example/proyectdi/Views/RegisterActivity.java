package com.example.proyectdi.Views;



import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

import com.example.proyectdi.R;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class RegisterActivity extends AppCompatActivity {
    //inicializar variables
    private EditText editTextFullName, editTextEmail, editTextPassword, editTextPassworConfirm, editTextPhone, editTextAddress;
    private FirebaseAuth mAuth;
    private Button button;
    private final Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //mostrar activity
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_register);

        //dar valores a las variables
        editTextFullName = findViewById(R.id.fullNameEditText);
        editTextEmail = findViewById(R.id.emailEditText);
        editTextPassword = findViewById(R.id.passwordEditText);
        editTextPassworConfirm = findViewById(R.id.passwordConfirmEditText);
        editTextPhone = findViewById(R.id.phoneEditText);
        editTextAddress = findViewById(R.id.addressEditText);
        button = findViewById(R.id.registerButton);
        // Inicializa FirebaseAuth para el manejo de autenticación
        mAuth = FirebaseAuth.getInstance();

        //cuando el boton sea pulsado ir a registerUser
        button.setOnClickListener(v -> registerUser());
    }

    private void registerUser(){
        //comprobar que todos los parámetros este cubiertos
        if (editTextFullName.length() <= 0 || editTextPassword.length() <= 0 || editTextPassworConfirm.length() <= 0 || editTextPhone.length() <= 0 || editTextAddress.length() <= 0) {
            Toast.makeText(context, "All parameters must be covered.", Toast.LENGTH_SHORT).show();
        }
        //comprobar que laa confirmacion de la contraseña sea igual a la contraseña
        else if (!editTextPassword.getText().toString().equals(editTextPassworConfirm.getText().toString())) {
            Toast.makeText(context, "Password confirmation is wrong", Toast.LENGTH_SHORT).show();
        }else {
            //crear un nuevo usuario en firebase con gmail y contraseña, toast de error y éxito
            mAuth.createUserWithEmailAndPassword(editTextEmail.getText().toString(), editTextPassword.getText().toString()).addOnCompleteListener(this, task -> {
                if (task.isSuccessful()) {

                    // Si la creación fue exitosa, obtener el usuario registrado
                    FirebaseUser firebaseUser = mAuth.getCurrentUser();
                    if (firebaseUser != null) {
                        String uid = firebaseUser.getUid(); // Obtener el ID del usuario

                        // Crear un objeto con los datos adicionales
                        User newUser = new User(uid,
                                editTextFullName.getText().toString(),
                                editTextEmail.getText().toString(),
                                editTextPhone.getText().toString(),
                                editTextAddress.getText().toString());
                        DatabaseReference databaseRef = FirebaseDatabase
                                .getInstance("https://proyecto-di-26dcb-default-rtdb.europe-west1.firebasedatabase.app")
                                .getReference("users");

                        // Guardar los datos del usuario en la base de datos bajo el UID
                        databaseRef.child(uid).setValue(newUser)
                                .addOnCompleteListener(dbTask -> {
                                    if (dbTask.isSuccessful()) {
                                        Log.d("Firebase", "Usuario añadido a Realtime Database con UID: " + uid);
                                        Toast.makeText(context, "Usuario registrado correctamente.", Toast.LENGTH_SHORT).show();
                                        finish(); // Cerrar la actividad de registro
                                    } else {
                                        Log.e("Firebase", "Error al añadir usuario a la base de datos", dbTask.getException());
                                        Toast.makeText(context, "Error al guardar los datos en la base de datos.", Toast.LENGTH_SHORT).show();
                                    }
                                });
                    }
                } else {
                    // Si hay un error en el registro, mostrar el mensaje de error
                    Log.e("Firebase", "Error al registrar usuario", task.getException());
                    Toast.makeText(RegisterActivity.this, "Error en el registro: " + task.getException().getMessage(), Toast.LENGTH_SHORT).show();
                }
            });
        }}


    // Clase interna para manejar los datos adicionales del usuario
    public static class User {
        public String uid;
        public String fullName;
        public String email;
        public String phone;
        public String address;

        public User(String uid, String fullName, String email, String phone, String address) {
            this.uid = uid;
            this.fullName = fullName;
            this.email = email;
            this.phone = phone;
            this.address = address;
        }
    }
}