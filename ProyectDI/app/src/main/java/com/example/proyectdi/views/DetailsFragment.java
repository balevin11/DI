package com.example.proyectdi.views;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.bumptech.glide.Glide;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import com.example.proyectdi.R;
import com.example.proyectdi.databinding.FragmentDetailsBinding;
import com.example.proyectdi.viewmodels.DetailsViewModel;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

public class DetailsFragment extends Fragment {

    private boolean isFavorite = false;
    private FloatingActionButton fav;
    private DetailsViewModel detailsViewModel;
    private static final String ARG_TITULO = "titulo";
    private static final String ARG_DESCRIPCION = "descripcion";
    private static final String ARG_IMAGEN = "imagen";
    private static final String ARG_GAME_INDEX = "gameIndex";

    public DetailsFragment() {
    }
    public static DetailsFragment newInstance(String titulo, String descripcion, String imagen, int gameIndex) {
        DetailsFragment fragment = new DetailsFragment();
        Bundle args = new Bundle();
        args.putString(ARG_TITULO, titulo);
        args.putString(ARG_DESCRIPCION, descripcion);
        args.putString(ARG_IMAGEN, imagen);
        args.putInt(ARG_GAME_INDEX, gameIndex);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        FragmentDetailsBinding binding = FragmentDetailsBinding.inflate(inflater, container, false);
        View view = binding.getRoot();


        // Recuperar los argumentos, si existen
        if (getArguments() != null) {
            String titulo = getArguments().getString(ARG_TITULO);
            String descripcion = getArguments().getString(ARG_DESCRIPCION);
            String imagen = getArguments().getString(ARG_IMAGEN);
            int gameIndex = getArguments().getInt(ARG_GAME_INDEX);

            // Asignar valores a las vistas
            binding.gameName.setText(titulo);
            binding.gameDescription.setText(descripcion);

            // Cargar imagen con Glide
            Glide.with(this)
                    .load(imagen)
                    .into(binding.imageView);

            detailsViewModel =  new ViewModelProvider(this).get(DetailsViewModel.class);

            fav = binding.fav;
            detailsViewModel.getIsFavorite().observe(getViewLifecycleOwner(), isFavorite -> {
                this.isFavorite = isFavorite;
                if (isFavorite) {
                    fav.setImageResource(R.drawable.favorite);
                } else {
                    fav.setImageResource(R.drawable.favorite_border);
                }
            });
            // Verificar si el juego ya está en favoritos cuando se carga la actividad
            detailsViewModel.checkFavorite(gameIndex);

            // Guardar en favoritos
            fav.setOnClickListener(v -> {
                if (isFavorite) {
                    detailsViewModel.removeFavorite(gameIndex); // Eliminar de favoritos
                } else {
                    detailsViewModel.addFavorite(gameIndex); // Agregar a favoritos
                }
            });

        }
        return view;
    }
}