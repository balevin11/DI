package com.example.proyectdi.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.example.proyectdi.models.Games;
import com.example.proyectdi.repositories.DetailsRepository;
import com.google.firebase.auth.FirebaseAuth;

import java.util.List;

public class DetailsViewModel {
    //inicializar variables
    private final MutableLiveData<Games> gameLiveData = new MutableLiveData<>();
    private final DetailsRepository detailsRepository;

    //constructor
    public DetailsViewModel() {
        detailsRepository = new DetailsRepository();
        loadFavorite();
    }
    private void loadFavorite() {
        detailsRepository.getFavorite(gameLiveData);
    }

}
