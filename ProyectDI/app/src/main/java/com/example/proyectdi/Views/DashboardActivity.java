package com.example.proyectdi.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;

import android.widget.Toast;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import com.example.proyectdi.adapters.GamesAdapter;
import com.example.proyectdi.R;
import com.example.proyectdi.viewmodels.DashboardViewModel;
import com.example.proyectdi.databinding.ActivityDashboardBinding;
import java.util.ArrayList;

public class DashboardActivity extends AppCompatActivity {
    //inicializar variables
    private GamesAdapter gamesAdapter;
    private DashboardViewModel dashboardViewModel;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //mostrar activity
        super.onCreate(savedInstanceState);

        ActivityDashboardBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_dashboard);

        Button button = binding.logout;
        gamesAdapter = new GamesAdapter(new ArrayList<>());
        binding.recyclerView.setLayoutManager(new LinearLayoutManager(this));
        binding.recyclerView.setAdapter(gamesAdapter);

        dashboardViewModel = new ViewModelProvider(this).get(DashboardViewModel.class);
        dashboardViewModel.getGamesLiveData().observe(this, Games -> gamesAdapter.setGames(Games));

        //cuando se pulse el boton logout cerrar la actividad y la sesion
        button.setOnClickListener(v -> {
            dashboardViewModel.logout();
            Toast.makeText(DashboardActivity.this, "Sesión cerrada", Toast.LENGTH_SHORT).show();
            Intent intent = new Intent(DashboardActivity.this, LoginActivity.class);
            startActivity(intent);
            finish();
        });
    }
}