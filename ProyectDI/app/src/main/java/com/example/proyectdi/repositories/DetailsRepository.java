package com.example.proyectdi.repositories;

import android.util.Log;

import androidx.lifecycle.MutableLiveData;

import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class DetailsRepository {
    private final DatabaseReference userRef;
    private String uid;

    public DetailsRepository() {
        // Obtener la instancia de FirebaseAuth
        FirebaseAuth mAuth = FirebaseAuth.getInstance();

        // Obtener el usuario actual
        FirebaseUser user = mAuth.getCurrentUser();

        if (user != null) {
            // Si hay un usuario autenticado, obtenemos el UID
            uid = user.getUid();
            // Puedes usar el UID como lo necesites
            Log.d("UID", "El UID del usuario es: " + uid);
        } else {
            // Si no hay un usuario autenticado
            Log.d("UID", "No hay usuario autenticado.");
        }
        userRef = FirebaseDatabase.getInstance().getReference("users/"+ uid +"/favourites");

    }
    public void addFavorite(int gameIndex){
        userRef.child(String.valueOf(gameIndex)).setValue(true);
    }
    // Métod para eliminar el juego de favoritos
    public void removeGameFromFavorites(int juegoIndex) {
        userRef.child(String.valueOf(juegoIndex)).removeValue();
    }

    // Métod para verificar si el juego está en favoritos
    public Task<DataSnapshot> isGameFavorite(int juegoIndex) {
        return userRef.child(String.valueOf(juegoIndex)).get();
    }

}
