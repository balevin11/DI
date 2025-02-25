package com.example.proyectdi.adapters;

import android.view.LayoutInflater;
import android.view.ViewGroup;
import androidx.databinding.DataBindingUtil;
import androidx.recyclerview.widget.RecyclerView;
import com.bumptech.glide.Glide;
import com.example.proyectdi.R;
import com.example.proyectdi.databinding.AdapterFavouritesBinding;
import com.example.proyectdi.models.Games;
import org.checkerframework.checker.nullness.qual.NonNull;
import java.util.List;

public class FavouritesAdapter extends RecyclerView.Adapter<FavouritesAdapter.FavouritesViewHolder> {

    // Lista de objetos juegos que serán mostrados
    private List<Games> games;
    // Constructor
    public FavouritesAdapter(List<Games> games) {
        this.games = games;
    }

    // Métod para actualizar la lista de juegos y notificar al RecyclerView que los datos han cambiado
    public void setGames(List<Games> games) {
        this.games = games;
        notifyDataSetChanged();// Notifica al RecyclerView que los datos han cambiado
    }

    // Métod que crea un nuevo ViewHolder para cada item
    @NonNull
    @Override
    public FavouritesAdapter.FavouritesViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        // Inflar el layout usando DataBinding y obtener el binding correspondiente
        AdapterFavouritesBinding binding = DataBindingUtil.inflate(
                LayoutInflater.from(parent.getContext()),// Obtiene el LayoutInflater
                R.layout.adapter_favourites,// El layout XML que representa cada item
                parent,// El contenedor (ViewGroup) padre
                false// No se adjunta aún a la vista
        );
        return new FavouritesAdapter.FavouritesViewHolder(binding);// Retorna un nuevo ViewHolder con el binding
    }

    // Métod que vincula los datos del objeto Games con las vistas del ViewHolder
    @Override
    public void onBindViewHolder(@NonNull FavouritesAdapter.FavouritesViewHolder holder, int position) {
        // Obtener el objeto Games en la posición correspondiente de la lista
        Games game = games.get(position);
        // Usamos Glide para cargar la imagen desde la URL
        Glide.with(holder.itemView.getContext())
                .load(game.getImagen())
                .into(holder.binding.imageView);
        // Vincular el objeto de datos al ViewHolder
        holder.bind(game);
    }

    // Métod que retorna el número de elementos en la lista de juegos
    @Override
    public int getItemCount() {
        // Si la lista es null, retorna 0, sino retorna el tamaño de la lista
        return games != null ? games.size() : 0;
    }

    // Clase ViewHolder que mantiene el binding de cada item
    class FavouritesViewHolder extends RecyclerView.ViewHolder {
        // Variable para mantener el binding del layout de cada item
        private final AdapterFavouritesBinding binding;

        // Constructor del ViewHolder que recibe el binding de cada item
        public FavouritesViewHolder(AdapterFavouritesBinding binding) {
            super(binding.getRoot());// Llama al constructor de ViewHolder con la vista raíz
            this.binding = binding; // Asigna el binding a la variable
        }

        // Métod que asigna los datos al binding y actualiza las vistas
        public void bind(Games games) {
            // Asigna el objeto games al binding para que los datos se enlacen a las vistas
            binding.setGames(games);
            // Ejecuta cualquier enlace pendiente para asegurarse de que se actualicen las vistas
            binding.executePendingBindings();
        }

    }

}
