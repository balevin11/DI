package com.example.proyectdi.Views;

import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.example.proyectdi.R;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.checkerframework.checker.nullness.qual.NonNull;

public class Dashboard_Activity extends AppCompatActivity {
    //inicializar variables
    private ImageView image;
    private TextView titleTextView, descriptionTextView;
    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //mostrar activity
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_dashboard);
        //dar valores a las variables
        image = findViewById(R.id.imageView);
        Button button = findViewById(R.id.logout);
        titleTextView = findViewById(R.id.title);
        descriptionTextView = findViewById(R.id.description);
        mAuth = FirebaseAuth.getInstance();

        //cuando se pulse el boton logout cerrar la actividad y la sesion
        button.setOnClickListener(v -> {
            mAuth.signOut();
            Toast.makeText(Dashboard_Activity.this, "Sesión cerrada", Toast.LENGTH_SHORT).show();
            finish();});

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
                        Glide.with(Dashboard_Activity.this).load(imagenUrl).into(image);

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
}