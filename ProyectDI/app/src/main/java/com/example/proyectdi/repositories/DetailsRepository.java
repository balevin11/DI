package com.example.proyectdi.repositories;

import android.util.Log;

import androidx.lifecycle.MutableLiveData;

import com.example.proyectdi.models.Games;
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
        userRef = FirebaseDatabase.getInstance().getReference("user/n6saieEi64MbRnMmcm7D3yewN3i2/favourites");

    }
    public void addFavorite(){
        userRef.child("0").setValue(true);
    }
    public void getFavorite(MutableLiveData<List<Games>> gameLiveData){
        userRef.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                List<String> favorites = new ArrayList<>();
                for (DataSnapshot child : snapshot.getChildren()) {
                    favorites.add(child.getKey());
                }
                // Usar los favoritos
                gameLiveData.setValue(games);
            }

            @Override
            public void onCancelled(DatabaseError error) {
                // Manejo de errores
            }
        });
    }
}
