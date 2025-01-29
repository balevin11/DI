package com.example.proyectdi.Views;

import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import com.example.proyectdi.Adapters.GamesAdapter;
import com.example.proyectdi.R;
import com.example.proyectdi.ViewModels.DashboardViewModel;
import com.example.proyectdi.databinding.ActivityDashboardBinding;
import java.util.ArrayList;

public class DashboardActivity extends AppCompatActivity {
    //inicializar variables
    private ImageView image;
    private TextView titleTextView, descriptionTextView;
    private GamesAdapter gamesAdapter;
    private DashboardViewModel dashboardViewModel;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //mostrar activity
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
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
            finish();
        });


    }
}

/*
        // Obtener referencia a la base de datos de Firebase
        FirebaseDatabase database = FirebaseDatabase.getInstance("https://proyecto-di-26dcb-default-rtdb.europe-west1.firebasedatabase.app");
        DatabaseReference databaseRef = database.getReference("juegos");


            // Obtener datos del primer juego
            databaseRef.child("0").addListenerForSingleValueEvent(new ValueEventListener() {
                @Override
                public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                    if (dataSnapshot.exists()) {
                        // Obtener los datos del juego
                        String titulo = dataSnapshot.child("titulo").getValue(String.class);
                        String descripcion = dataSnapshot.child("descripcion").getValue(String.class);
                        String imagenUrl = dataSnapshot.child("imagen").getValue(String.class);

                        // Mostrar los datos en los TextView y ImageView
                        titleTextView.setText(titulo);
                        descriptionTextView.setText(descripcion);

                        // Usar Glide para cargar la imagen, para usar glide hace falta añadir una dependencia
                        Glide.with(DashboardActivity.this).load(imagenUrl).into(image);

                        // Agregar el log para ver la URL, el título y la descripción
                        Log.d("Firebase", "Título: " + titulo);
                        Log.d("Firebase", "Descripción: " + descripcion);
                        Log.d("Firebase", "URL de la imagen: " + imagenUrl);

                    } else {
                        Log.d("Firebase", "No hay datos en el nodo juegos.");
                    }
                }

                @Override
                public void onCancelled(@NonNull DatabaseError databaseError) {
                    Log.w("Firebase", "Error al leer datos", databaseError.toException());
                }
            });

    }
}*/