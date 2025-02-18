package com.example.proyectdi.viewmodels;

import androidx.lifecycle.ViewModel;
import com.example.proyectdi.repositories.MainRepository;

public class MainViewModel extends ViewModel {
    private final MainRepository mainRepository;

    //constructor
    public MainViewModel() {
        mainRepository = new MainRepository();
    }
    public void logout(){
        mainRepository.logout();
    }

}
