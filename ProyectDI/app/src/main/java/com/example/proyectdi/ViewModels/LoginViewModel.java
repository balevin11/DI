package com.example.proyectdi.ViewModels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.proyectdi.Repositories.UserRepository;

public class LoginViewModel extends ViewModel {
    //inicializar variables
    private final UserRepository userRepository;
    private final MutableLiveData<String> email = new MutableLiveData<>(),
                                        password = new MutableLiveData<>(),
                                        loginStatus = new MutableLiveData<>();

    //constructor
    public LoginViewModel() {
        userRepository = new UserRepository();
        loginUser();
    }

    // LiveData para el estado del login (éxito o error)
    public LiveData<String> getLoginStatus() {
        return loginStatus;
    }

    // Método para recibir los datos del formulario
    public void setLoginDetails(String email, String password) {
        this.email.setValue(email);
        this.password.setValue(password);

        // Llamar al método para iniciar sesion
        loginUser();
    }


    public void loginUser(){
        //comprobar que todos los parámetros este cubiertos
        if (email.getValue() == null ||password.getValue() == null ||
                email.getValue().isEmpty() || password.getValue().isEmpty()) {
            loginStatus.setValue("Todos los campos son obligatorios.");
            return;
        }
        userRepository.LoginUser(email.getValue(),password.getValue(),new UserRepository.LoginCallback() {
            @Override
            public void onSuccess() {
                loginStatus.setValue("Sesión iniciada.");
            }

            @Override
            public void onFailure(String errorMessage) {
                loginStatus.setValue("Error al iniciar sesión: " + errorMessage);
            }

        });
    }
}

