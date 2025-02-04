package com.example.proyectdi.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import com.example.proyectdi.R;
import com.example.proyectdi.adapters.GamesAdapter;
import com.example.proyectdi.databinding.ActivityDetailsBinding;
import com.example.proyectdi.viewmodels.DashboardViewModel;

import java.util.ArrayList;

public class DetailsActivity extends AppCompatActivity {

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
        }
    }
}