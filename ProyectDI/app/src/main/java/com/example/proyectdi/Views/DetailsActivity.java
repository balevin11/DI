package com.example.proyectdi.views;

import android.content.Intent;
import android.os.Bundle;
import com.example.proyectdi.models.Games;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import com.example.proyectdi.R;
import com.example.proyectdi.adapters.GamesAdapter;
import com.example.proyectdi.databinding.ActivityDetailsBinding;

public class DetailsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActivityDetailsBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_details);

        binding.getRoot().setOnClickListener(v -> GamesAdapter.OnGamesClickListener.onGamesClick(Games));

        GamesAdapter adapter = new GamesAdapter(new ArrayList<>(), game -> {
            Intent intent = new Intent(this, DetailsActivity.class);
            intent.putExtra("title", game.getTitulo());
            intent.putExtra("description", game.getDescripcion());
            intent.putExtra("imageUrl", game.getImagen());
            startActivity(intent);
        });
    }
}