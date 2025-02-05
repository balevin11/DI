package com.example.proyectdi.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.proyectdi.models.Games;
import com.example.proyectdi.repositories.DashboardRepository;
import com.google.firebase.auth.FirebaseAuth;

import java.util.List;

public class DashboardViewModel extends ViewModel {
    //inicializar variables
    private final MutableLiveData<List<Games>> gamesLiveData = new MutableLiveData<>();
    private final DashboardRepository dashboardRepository;

    //constructor
    public DashboardViewModel() {
        dashboardRepository = new DashboardRepository();
        loadGamess();
    }

    // LiveData para mandar los datos
    public LiveData<List<Games>> getGamesLiveData() {
        return gamesLiveData;
    }

    //obtener los juegos
    private void loadGamess() {
        dashboardRepository.getGames(gamesLiveData);
    }

    public void logout(){
        FirebaseAuth mAuth = FirebaseAuth.getInstance();
        mAuth.signOut();
    }

}

