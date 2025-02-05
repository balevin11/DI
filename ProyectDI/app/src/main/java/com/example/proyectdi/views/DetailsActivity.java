package com.example.proyectdi.views;

import android.content.Intent;
import android.os.Bundle;
import com.bumptech.glide.Glide;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import com.example.proyectdi.R;
import com.example.proyectdi.databinding.ActivityDetailsBinding;
import com.google.android.material.floatingactionbutton.FloatingActionButton;


public class DetailsActivity extends AppCompatActivity {

    private boolean isFavorite = false;

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

            // Asignar valores a las vistas
            binding.gameName.setText(titulo);
            binding.gameDescription.setText(descripcion);

            // Cargar imagen con Glide
            Glide.with(this)
                    .load(imagen)
                    .into(binding.imageView);

            FloatingActionButton fav = binding.fav;
            fav.setOnClickListener(view -> {
                if (isFavorite) {
                    fav.setImageResource(R.drawable.favorite_border);  // Cambiar a favorite_border
                } else {
                    fav.setImageResource(R.drawable.favorite);  // Cambiar a favorite
                }
                isFavorite = !isFavorite;  // Alternar el estado
            });
        }

    }
}