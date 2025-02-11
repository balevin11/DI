package com.example.proyectdi.views;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;

import com.example.proyectdi.R;
import com.example.proyectdi.adapters.GamesAdapter;
import com.example.proyectdi.viewmodels.DashboardViewModel;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.example.proyectdi.databinding.FragmentDashboardBinding;
import java.util.ArrayList;

public class DashboardFragment extends Fragment {
    private GamesAdapter gamesAdapter;

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        FragmentDashboardBinding binding = FragmentDashboardBinding.inflate(inflater, container, false);
        View view = binding.getRoot();

        // Configuración del modo oscuro basado en SharedPreferences
        SharedPreferences sharedPrefs = requireActivity().getSharedPreferences("AppConfig", Context.MODE_PRIVATE);
        boolean darkModes = sharedPrefs.getBoolean("darkMode", false);
        if (darkModes) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }



        // Inicializar el adapter con un listener que lanza DetailsFragment
        gamesAdapter = new GamesAdapter(new ArrayList<>(), (game, position) -> {
            // Crear el Intent para lanzar DetailsFragment
            DetailsFragment detailsFragment = DetailsFragment.newInstance(
                    game.getTitulo(),
                    game.getDescripcion(),
                    game.getImagen(),
                    position
            );
            // Se realiza la transacción para reemplazar el fragmento actual por DetailsFragment
            FragmentTransaction transaction = getParentFragmentManager().beginTransaction();
            transaction.replace(R.id.fragment_container, detailsFragment);
            transaction.addToBackStack(null); // Permite volver al DashboardFragment al presionar "Atrás"
            transaction.commit();
        });

        binding.recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        binding.recyclerView.setAdapter(gamesAdapter);

        // Observa el LiveData para actualizar la lista de juegos
        DashboardViewModel dashboardViewModel = new ViewModelProvider(this).get(DashboardViewModel.class);
        dashboardViewModel.getGamesLiveData().observe(getViewLifecycleOwner(), games -> {
            if (games != null) {
                gamesAdapter.setGames(games); // Actualiza la lista del RecyclerView
            } else {
                Toast.makeText(getContext(), "Failed to load games.", Toast.LENGTH_SHORT).show();
            }
        });

        // Alterna el modo oscuro y recrea la actividad para aplicar el cambio
        FloatingActionButton darkMode = binding.darkMode;
        darkMode.setOnClickListener(v -> {
            // si darkmode está activado
            SharedPreferences sharedPref = requireActivity().getSharedPreferences("AppConfig", Context.MODE_PRIVATE);
            boolean isDarkMode = sharedPref.getBoolean("darkMode", false);
            SharedPreferences.Editor editors = sharedPref.edit();
            editors.putBoolean("darkMode", !isDarkMode);
            editors.apply();
            requireActivity().recreate();
        });
        return view;
    }


}