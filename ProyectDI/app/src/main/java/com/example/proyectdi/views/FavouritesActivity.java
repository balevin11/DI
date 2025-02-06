package com.example.proyectdi.views;

import android.os.Bundle;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import com.example.proyectdi.R;
import com.example.proyectdi.adapters.FavouritesAdapter;
import com.example.proyectdi.databinding.ActivityFavouritesBinding;
import com.example.proyectdi.viewmodels.FavouritesViewModel;
import java.util.ArrayList;

public class FavouritesActivity extends AppCompatActivity {
    private FavouritesAdapter favouritesAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActivityFavouritesBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_favourites);

        favouritesAdapter = new FavouritesAdapter(new ArrayList<>());

        binding.recyclerViewFav.setLayoutManager(new LinearLayoutManager(this)); // Configura el RecyclerView
        binding.recyclerViewFav.setAdapter(favouritesAdapter); // Establece el adaptador

        FavouritesViewModel favouritesViewModel = new ViewModelProvider(this).get(FavouritesViewModel.class);
        favouritesViewModel.getGamesLiveData().observe(this, games -> {
            if (games != null) {
                favouritesAdapter.setGames(games); // Actualiza la lista del RecyclerView
            } else {
                Toast.makeText(FavouritesActivity.this, "Failed to load games.", Toast.LENGTH_SHORT).show();
            }
        });
    }
}