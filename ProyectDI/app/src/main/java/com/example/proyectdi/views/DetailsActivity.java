package com.example.proyectdi.views;

import android.content.Intent;
import android.os.Bundle;
import com.bumptech.glide.Glide;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import com.example.proyectdi.R;
import com.example.proyectdi.databinding.ActivityDetailsBinding;
import com.example.proyectdi.viewmodels.DetailsViewModel;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

public class DetailsActivity extends AppCompatActivity {

    private boolean isFavorite = false;
    private FloatingActionButton fav;
    private DetailsViewModel detailsViewModel;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActivityDetailsBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_details);


        // Obtener datos del Intent
        Intent intent = getIntent();
        if (intent != null) {
            String titulo = intent.getStringExtra("titulo");
            String descripcion = intent.getStringExtra("descripcion");
            String imagen = intent.getStringExtra("imagen");
            int gameIndex = intent.getIntExtra("gameIndex", -1);

            // Asignar valores a las vistas
            binding.gameName.setText(titulo);
            binding.gameDescription.setText(descripcion);

            // Cargar imagen con Glide
            Glide.with(this)
                    .load(imagen)
                    .into(binding.imageView);

            detailsViewModel =  new ViewModelProvider(this).get(DetailsViewModel.class);

            fav = binding.fav;
            detailsViewModel.getIsFavorite().observe(this, isFavorite -> {
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
            fav.setOnClickListener(view -> {
                if (isFavorite) {
                    detailsViewModel.removeFavorite(gameIndex); // Eliminar de favoritos
                } else {
                    detailsViewModel.addFavorite(gameIndex); // Agregar a favoritos
                }
            });

        }

    }
}