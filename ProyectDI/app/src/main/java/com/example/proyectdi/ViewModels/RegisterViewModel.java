package com.example.proyectdi.ViewModels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.proyectdi.Repositories.UserRepository;

public class RegisterViewModel extends ViewModel {
    private final MutableLiveData<String> registrationStatus = new MutableLiveData<>();  // Para indicar el estado del registro
    private final UserRepository userRepository;
    private String email, password, passwordConfirm, fullName, address,phone;
    public RegisterViewModel(String email, String password,String passwordConfirm, String fullName, String address, String phone) {
        userRepository = new UserRepository();
        this.email = email;
        this.password = password;
        this.passwordConfirm = passwordConfirm;
        this.fullName = fullName;
        this.address = address;
        this.phone = phone;
        registerUsers();
    }

    // LiveData para el estado del registro (éxito o error)
    public LiveData<String> getRegistrationStatus() {
        return registrationStatus;
    }

    private void registerUsers() {
        //comprobar que todos los parámetros este cubiertos
        if (email.isEmpty() || fullName.isEmpty() || password.isEmpty() || passwordConfirm.isEmpty() || phone.isEmpty() || address.isEmpty()) {
            registrationStatus.setValue("Todos los campos son obligatorios.");

        }
        //comprobar que laa confirmacion de la contraseña sea igual a la contraseña
        else if (!password.equals(passwordConfirm)) {
            registrationStatus.setValue("La confirmación tiene que ser igual a la contraseña.");

        }else {
            userRepository.setUser(email, password,fullName,address, Integer.parseInt(phone), new UserRepository.RegistrationCallback(){
                @Override
                public void onSuccess() {
                    registrationStatus.setValue("Registro exitoso.");
                }
                @Override
                public void onFailure(String errorMessage) {
                    registrationStatus.setValue("Error al registrar: " + errorMessage);
                }
            });
        }
    }
}

