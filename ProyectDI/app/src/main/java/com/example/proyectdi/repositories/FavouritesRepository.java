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

public class FavouritesRepository {

    private final DatabaseReference gamesRef, userFavouritesRef;
    private String uid;
    public FavouritesRepository() {
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
        userFavouritesRef = FirebaseDatabase.getInstance().getReference("users/"+ uid +"/favourites");
        gamesRef = FirebaseDatabase.getInstance().getReference("juegos");
    }
    public void getFavorites(MutableLiveData<List<String>> favouritesLiveData){
        userFavouritesRef.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                List<String> favorites = new ArrayList<>();
                for (DataSnapshot child : snapshot.getChildren()) {
                    favorites.add(child.getKey());
                }
                favouritesLiveData.setValue(favorites);
            }

            @Override
            public void onCancelled(DatabaseError error) {
                // Manejo de errores
            }
        });
    }
    // Obtener los juegos favoritos (usando las posiciones que vienen de getFavorites)
    public void getGames(List<String> favouritesList, MutableLiveData<List<Games>> gamesLiveData) {
        List<Games> favoriteGames = new ArrayList<>();

        // Recorrer la lista de favoritos (que contiene los IDs de los juegos)
        for (String favPos : favouritesList) {
            // Convertir la posición de favorito a índice
            int position = Integer.parseInt(favPos);

            // Obtener el juego correspondiente de Firebase usando el índice
            gamesRef.child(String.valueOf(position)).addListenerForSingleValueEvent(new ValueEventListener() {
                @Override
                public void onDataChange(DataSnapshot snapshot) {
                    Games game = snapshot.getValue(Games.class);
                    if (game != null) {
                        // Si el juego existe, lo añadimos a la lista de juegos favoritos
                        favoriteGames.add(game);
                    }

                    // Después de agregar todos los juegos favoritos, actualizamos el LiveData
                    if (favoriteGames.size() == favouritesList.size()) {
                        gamesLiveData.setValue(favoriteGames);
                    }
                }

                @Override
                public void onCancelled(DatabaseError error) {
                    Log.e("Firebase", "Error al obtener el juego favorito", error.toException());
                }
            });
        }
    }
}
