package com.example.proyectdi.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.proyectdi.repositories.DetailsRepository;

public class DetailsViewModel extends ViewModel {
    //inicializar variables
    private final DetailsRepository detailsRepository;
    private final MutableLiveData<Boolean> isFavorite = new MutableLiveData<>();
    //constructor
    public DetailsViewModel() {
        detailsRepository = new DetailsRepository();
    }


    // Verificar si el juego está en favoritos
    public void checkFavorite(int juegoIndex) {
        detailsRepository.isGameFavorite(juegoIndex).addOnCompleteListener(task -> {
            if (task.isSuccessful()) {
                // Si el juego existe en Firebase, es un favorito
                isFavorite.setValue(task.getResult().exists());
            }
        });
    }
    // Agregar juego a favoritos
    public void addFavorite(int juegoIndex) {
        detailsRepository.addFavorite(juegoIndex);
        isFavorite.setValue(true);
    }
    // Eliminar juego de favoritos
    public void removeFavorite(int juegoIndex) {
        detailsRepository.removeGameFromFavorites(juegoIndex);
        isFavorite.setValue(false);
    }

    public LiveData<Boolean> getIsFavorite() {
        return isFavorite;
    }

}
