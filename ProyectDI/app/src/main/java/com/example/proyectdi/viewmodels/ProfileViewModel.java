package com.example.proyectdi.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.proyectdi.repositories.ProfileRepository;

public class ProfileViewModel extends ViewModel {
    //inicializar variables
    private final ProfileRepository profileRepository;
    private final MutableLiveData<String> password_actual = new MutableLiveData<>(),
            password_new = new MutableLiveData<>(),
            changePasswordStatus = new MutableLiveData<>();

    //constructor
    public ProfileViewModel() {
        profileRepository = new ProfileRepository();

    }

    // LiveData para el estado del changePassword (éxito o error)
    public LiveData<String> getChangePasswordStatus() {
        return changePasswordStatus;
    }

    // Métod para recibir los datos del formulario
    public void setChangePasswordDetails(String password_new, String password_actual) {
        this.password_new.setValue(password_new);
        this.password_actual.setValue(password_actual);

        // Llamar al métod para cambiar contraseña
        changePassword();
    }


    public void changePassword(){
        //changePasswordStatus igual a hola para evitar repeticiones
        changePasswordStatus.setValue("hola");
        //comprobar que todos los parámetros este cubiertos
        if (password_actual.getValue() == null ||password_new.getValue() == null ||
                password_actual.getValue().isEmpty() || password_new.getValue().isEmpty()) {
            changePasswordStatus.setValue("Todos los campos son obligatorios.");

            return;
        }
        profileRepository.changePassword(password_new.getValue(),password_actual.getValue(),new ProfileRepository.changeCallback() {
            @Override
            public void onSuccess() {
                changePasswordStatus.setValue("Contraseña cambiada");

            }
            @Override
            public void onFailure(String errorMessage) {
                changePasswordStatus.setValue("Error al cambiar la contraseña: " + errorMessage);

            }

        });
    }
}