package com.example.proyectdi.Repositories;

import androidx.lifecycle.MutableLiveData;
import com.example.proyectdi.Models.Games;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import java.util.ArrayList;
import java.util.List;

public class DashboardRepository {

    private final DatabaseReference gamesRef;

    public DashboardRepository() {
        gamesRef = FirebaseDatabase.getInstance().getReference("juegos");
    }

    public void getGames(MutableLiveData<List<Games>> gamesLiveData) {
        gamesRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot snapshot) {
                List<Games> games = new ArrayList<>();
                for (DataSnapshot child : snapshot.getChildren()) {
                    Games game = child.getValue(Games.class);
                    games.add(game);
                }
                gamesLiveData.setValue(games);
            }

            @Override
            public void onCancelled(DatabaseError error) {
                // Manejo de errores
            }
        });
    }
}
