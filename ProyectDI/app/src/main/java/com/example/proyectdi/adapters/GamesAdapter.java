package com.example.proyectdi.adapters;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.ViewGroup;
import androidx.databinding.DataBindingUtil;
import androidx.recyclerview.widget.RecyclerView;
import com.bumptech.glide.Glide;
import com.example.proyectdi.databinding.AdapterGamesBinding;
import com.example.proyectdi.models.Games;
import com.example.proyectdi.R;

import org.checkerframework.checker.nullness.qual.NonNull;
import java.util.List;

public class GamesAdapter extends RecyclerView.Adapter<GamesAdapter.GamesViewHolder> {

    // Lista de objetos juegos que serán mostrados
    private List<Games> games;
    private OnGameClickListener listener;

    // Constructor
    public GamesAdapter(List<Games> games) {
        this.games = games;
    }
    public GamesAdapter(List<Games> games, OnGameClickListener listener) {
        this.games = games;
        this.listener = listener;
    }

    // Métod para actualizar la lista de juegos y notificar al RecyclerView que los datos han cambiado
    public void setGames(List<Games> games) {
        this.games = games;
        notifyDataSetChanged();// Notifica al RecyclerView que los datos han cambiado
    }

    // Métod que crea un nuevo ViewHolder para cada item
    @NonNull
    @Override
    public GamesViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Inflar el layout usando DataBinding y obtener el binding correspondiente
        AdapterGamesBinding binding = DataBindingUtil.inflate(
                LayoutInflater.from(parent.getContext()),// Obtiene el LayoutInflater
                R.layout.adapter_games,// El layout XML que representa cada item
                parent,// El contenedor (ViewGroup) padre
                false// No se adjunta aún a la vista
        );
        return new GamesViewHolder(binding);// Retorna un nuevo ViewHolder con el binding
    }

    // Métod que vincula los datos del objeto Games con las vistas del ViewHolder
    @Override
    public void onBindViewHolder(@NonNull GamesViewHolder holder, int position) {
        Games game = games.get(position);
        // Cargar la imagen usando Glide
        Glide.with(holder.itemView.getContext())
                .load(game.getImagen())
                .into(holder.binding.imageView);
        // Delegar el bind, el cual configura el listener
        holder.bind(game, position);
    }

    // Métod que retorna el número de elementos en la lista de juegos
    @Override
    public int getItemCount() {
        // Si la lista es null, retorna 0, sino retorna el tamaño de la lista
        return games != null ? games.size() : 0;
    }

    // Clase ViewHolder que mantiene el binding de cada item
    class GamesViewHolder extends RecyclerView.ViewHolder {
        // Variable para mantener el binding del layout de cada item
        private final AdapterGamesBinding binding;

        // Constructor del ViewHolder que recibe el binding de cada item
        public GamesViewHolder(@NonNull AdapterGamesBinding binding) {
            super(binding.getRoot());// Llama al constructor de ViewHolder con la vista raíz
            this.binding = binding; // Asigna el binding a la variable
        }

        // Métod que asigna los datos al binding y actualiza las vistas
        public void bind(Games games, int position) {
            // Asigna el objeto games al binding para que los datos se enlacen a las vistas
            binding.setGames(games);
            // Ejecuta cualquier enlace pendiente para asegurarse de que se actualicen las vistas
            binding.executePendingBindings();
            if (listener != null) {
                binding.getRoot().setOnClickListener(v -> listener.onGameClick(games, position));
            } else {
                Log.e("GamesAdapter", "Listener is null!");
            }
        }

    }
    public interface OnGameClickListener {
        void onGameClick(Games game, int position);
    }
}

