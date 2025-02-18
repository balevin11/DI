package com.example.proyectdi.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import com.example.proyectdi.R;
import androidx.databinding.DataBindingUtil;
import androidx.fragment.app.Fragment;
import androidx.appcompat.app.AppCompatActivity;
import com.example.proyectdi.databinding.ActivityMainBinding;
import com.example.proyectdi.viewmodels.MainViewModel;

public class MainActivity extends AppCompatActivity {

    private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = DataBindingUtil.setContentView(this, R.layout.activity_main);

        // Manejamos los eventos del menú lateral
        binding.navigationView.setNavigationItemSelectedListener(item -> {
            int id = item.getItemId();
            if (id == R.id.nav_dashboard) {
                openFragment(new DashboardFragment());
            } else if (id == R.id.nav_favorite) {
                openFragment(new FavouritesFragment());
            } else if (id == R.id.nav_profile) {
                openFragment(new ProfileFragment());
            } else if (id == R.id.nav_logout) {
                logoutUser();
            }
            // Al pulsar en un ítem, cerramos el drawer
            binding.drawerLayout.closeDrawers();
            return true;
        });

        // Cargar por defecto el DashboardFragment
        if (savedInstanceState == null) {
            openFragment(new DashboardFragment());
        }
    }

    private void openFragment(Fragment fragment) {
        getSupportFragmentManager()
                .beginTransaction()
                .replace(R.id.fragment_container, fragment)
                .commit();
    }

    private void logoutUser() {
        MainViewModel mainViewModel = new MainViewModel();
        mainViewModel.logout();
        Toast.makeText(this, "Sesión cerrrada", Toast.LENGTH_SHORT).show();
        // Redireccionar a LoginActivity
        Intent intent = new Intent(this, LoginActivity.class);
        startActivity(intent);
        finish(); // Para que no pueda volver con el botón atrás
    }
}