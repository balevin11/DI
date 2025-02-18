package com.example.proyectdi.repositories;

import static java.security.AccessController.getContext;

import android.widget.Toast;

import com.example.proyectdi.models.User;
import com.google.firebase.auth.AuthCredential;
import com.google.firebase.auth.EmailAuthProvider;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.Objects;

public class ProfileRepository {;
    private  FirebaseUser user;
    //constructor
    public ProfileRepository() {
        user = FirebaseAuth.getInstance().getCurrentUser();
    }

    public void changePassword(String newPass, String currentPass, changeCallback callback){
        if (user != null && !newPass.isEmpty()) {
            // EJEMPLO: reautenticación con la credencial actual (si quieres ser estricto con la seguridad)
            AuthCredential credential = EmailAuthProvider
                    .getCredential(Objects.requireNonNull(user.getEmail()), currentPass);

            user.reauthenticate(credential).addOnCompleteListener(task -> {
                if (task.isSuccessful()) {
                    user.updatePassword(newPass).addOnCompleteListener(updateTask -> {
                        if (updateTask.isSuccessful()) {
                            callback.onSuccess();
                        } else {
                            callback.onFailure("Error.");
                        }
                    });
                } else {
                    callback.onFailure("Contraseña actual invalida");
                }
            });
        }
    }

    // Interfaz para devolver el resultado del cambio de contraseña
    public interface changeCallback {
        void onSuccess();
        void onFailure(String errorMessage);
    }

}