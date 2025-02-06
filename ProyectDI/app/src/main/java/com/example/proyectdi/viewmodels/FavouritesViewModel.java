package com.example.proyectdi.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.proyectdi.models.Games;
import com.example.proyectdi.repositories.FavouritesRepository;

import java.util.List;

public class FavouritesViewModel extends ViewModel {
    //inicializar variables
    private final MutableLiveData<List<Games>> gamesLiveData = new MutableLiveData<>();
    private final FavouritesRepository favouritesRepository;

    //constructor
    public FavouritesViewModel() {
        favouritesRepository = new FavouritesRepository();
        loadFavorites();

    }

    // LiveData para mandar los datos
    public LiveData<List<Games>> getGamesLiveData() {
        return gamesLiveData;
    }


    // Métod para cargar los favoritos y obtener los juegos correspondientes
    private void loadFavorites() {
        MutableLiveData<List<String>> favouritesLiveData = new MutableLiveData<>();
        favouritesRepository.getFavorites(favouritesLiveData); // Obtiene los favoritos

        favouritesLiveData.observeForever(favourites -> {
            if (favourites != null && !favourites.isEmpty()) {
                // Si hay favoritos, obtenemos los juegos correspondientes
                favouritesRepository.getGames(favourites, gamesLiveData);
            }
        });
    }

}
