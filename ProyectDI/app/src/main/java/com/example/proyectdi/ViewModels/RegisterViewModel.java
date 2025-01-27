package com.example.proyectdi.ViewModels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.proyectdi.Repositories.UserRepository;

public class RegisterViewModel extends ViewModel {
    //inicializar variables
    private final UserRepository userRepository;
    private final MutableLiveData<String> email = new MutableLiveData<>(),
                                        password= new MutableLiveData<>(),
                                        passwordConfirm = new MutableLiveData<>(),
                                        fullName = new MutableLiveData<>(),
                                        address = new MutableLiveData<>(),
                                        phone = new MutableLiveData<>(),
                                        registrationStatus = new MutableLiveData<>();

    //constructor
    public RegisterViewModel() {
        userRepository = new UserRepository();
        registerUsers();
    }

    // LiveData para el estado del registro (éxito o error)
    public LiveData<String> getRegistrationStatus() {
        return registrationStatus;
    }

    // Método para recibir los datos del formulario
    public void setRegistrationDetails(String fullName, String email, String password, String passwordConfirm, String phone, String address) {
        this.fullName.setValue(fullName);
        this.email.setValue(email);
        this.password.setValue(password);
        this.passwordConfirm.setValue(passwordConfirm);
        this.phone.setValue(phone);
        this.address.setValue(address);

        // Llamar al método para registrar
        registerUsers();
    }

    private void registerUsers() {
        //comprobar que todos los parámetros este cubiertos
        if (email.getValue() == null || fullName.getValue() == null || password.getValue() == null ||
                passwordConfirm.getValue() == null || phone.getValue() == null || address.getValue() == null ||
                email.getValue().isEmpty() || fullName.getValue().isEmpty() || password.getValue().isEmpty() ||
                passwordConfirm.getValue().isEmpty() || phone.getValue().isEmpty() || address.getValue().isEmpty()) {

            registrationStatus.setValue("Todos los campos son obligatorios.");
            return;
        }
        //comprobar que laa confirmacion de la contraseña sea igual a la contraseña
        if (!password.getValue().equals(passwordConfirm.getValue())) {
            registrationStatus.setValue("La confirmación tiene que ser igual a la contraseña.");
            return;
        }
        int phone_num = 0;
        try {
            phone_num = Integer.parseInt(phone.getValue());
        } catch (NumberFormatException e) {
            registrationStatus.setValue("El número de teléfono no es válido.");
            return;
        }
        userRepository.setUser(email.getValue(), password.getValue(), fullName.getValue(), address.getValue(), phone_num, new UserRepository.RegistrationCallback() {
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

