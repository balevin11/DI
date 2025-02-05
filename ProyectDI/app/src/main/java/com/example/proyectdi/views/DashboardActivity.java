package com.example.proyectdi.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import com.example.proyectdi.adapters.GamesAdapter;
import com.example.proyectdi.R;
import com.example.proyectdi.models.Games;
import com.example.proyectdi.viewmodels.DashboardViewModel;
import com.example.proyectdi.databinding.ActivityDashboardBinding;

import java.util.ArrayList;

public class DashboardActivity extends AppCompatActivity implements GamesAdapter.OnGameClickListener{
    //inicializar variables
    private GamesAdapter gamesAdapter;
    private DashboardViewModel dashboardViewModel;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //mostrar activity
        super.onCreate(savedInstanceState);

        ActivityDashboardBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_dashboard);

        Button button = binding.logout;
        gamesAdapter = new GamesAdapter(new ArrayList<>(),this);
        binding.recyclerView.setLayoutManager(new LinearLayoutManager(this));
        binding.recyclerView.setAdapter(gamesAdapter);

        dashboardViewModel = new ViewModelProvider(this).get(DashboardViewModel.class);
        dashboardViewModel.getGamesLiveData().observe(this, games -> {
            if (games != null) {
                gamesAdapter.setGames(games); // Actualiza la lista del RecyclerView
            } else {
                Toast.makeText(DashboardActivity.this, "Failed to load games.", Toast.LENGTH_SHORT).show();
            }
        });

        //cuando se pulse el boton logout cerrar la actividad y la sesion
        button.setOnClickListener(v -> {
            dashboardViewModel.logout();
            Toast.makeText(DashboardActivity.this, "Sesión cerrada", Toast.LENGTH_SHORT).show();
            Intent intent = new Intent(DashboardActivity.this, LoginActivity.class);
            startActivity(intent);
            finish();
        });
    }
        @Override
        public void onGameClick(Games game) {
            // Crear un Intent para ir a DetailsActivity
            Intent intent = new Intent(DashboardActivity.this, DetailsActivity.class);

            // Pasar los datos del juego seleccionado (título, descripción e imagen)
            intent.putExtra("titulo", game.getTitulo());
            intent.putExtra("descripcion", game.getDescripcion());
            intent.putExtra("imagen", game.getImagen());

            // Iniciar la actividad DetailsActivity
            startActivity(intent);
        }

}