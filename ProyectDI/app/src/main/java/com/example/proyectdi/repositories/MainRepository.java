package com.example.proyectdi.repositories;

import com.google.firebase.auth.FirebaseAuth;

public class MainRepository {

    public MainRepository(){}

    //desloguearse
    public void logout(){
         FirebaseAuth.getInstance().signOut();
    }
}
            // Obtener el usuario actual