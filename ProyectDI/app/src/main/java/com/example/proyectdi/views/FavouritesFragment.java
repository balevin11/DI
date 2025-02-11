package com.example.proyectdi.views;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import com.example.proyectdi.adapters.FavouritesAdapter;
import com.example.proyectdi.databinding.FragmentFavouritesBinding;
import com.example.proyectdi.viewmodels.FavouritesViewModel;
import java.util.ArrayList;

public class FavouritesFragment extends Fragment {
    public FavouritesFragment() { }
    private FavouritesAdapter favouritesAdapter;

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        FragmentFavouritesBinding binding = FragmentFavouritesBinding.inflate(inflater, container, false);
        View view = binding.getRoot();


        favouritesAdapter = new FavouritesAdapter(new ArrayList<>());

        binding.recyclerViewFav.setLayoutManager(new LinearLayoutManager(getContext())); // Configura el RecyclerView
        binding.recyclerViewFav.setAdapter(favouritesAdapter); // Establece el adaptador

        FavouritesViewModel favouritesViewModel = new ViewModelProvider(this).get(FavouritesViewModel.class);
        favouritesViewModel.getGamesLiveData().observe(getViewLifecycleOwner(), games -> {
            if (games != null) {
                favouritesAdapter.setGames(games); // Actualiza la lista del RecyclerView
            } else {
                Toast.makeText(getContext(), "Failed to load games.", Toast.LENGTH_SHORT).show();
            }
        });
        return view;
    }
}