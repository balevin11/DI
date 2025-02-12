package com.example.proyectdi.views;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Switch;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatDelegate;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.LifecycleOwner;
import androidx.lifecycle.ViewModelProvider;

import com.example.proyectdi.R;
import com.example.proyectdi.databinding.FragmentProfileBinding;
import com.example.proyectdi.viewmodels.ProfileViewModel;


import org.checkerframework.checker.nullness.qual.NonNull;

public class ProfileFragment extends Fragment {

    private EditText currentPasswordEditText, newPasswordEditText;
    public ProfileFragment() { }
    private ProfileViewModel profileViewModel;
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        FragmentProfileBinding binding = FragmentProfileBinding.inflate(inflater, container, false);
        View view = binding.getRoot();
        currentPasswordEditText = binding.currentPasswordEditText;
        newPasswordEditText = binding.newPasswordEditText;
        @SuppressLint("UseSwitchCompatOrMaterialCode") Switch darkModeSwitch = binding.darkMode;

        // Estado inicial del switch (obtener de SharedPreferences)
        SharedPreferences prefs = requireActivity().getSharedPreferences("AppConfig", Context.MODE_PRIVATE);
        boolean isDarkMode = prefs.getBoolean("darkMode", false);
        darkModeSwitch.setChecked(isDarkMode);

        // Listener para botón "Cambiar contraseña"
        Button changePasswordButton = view.findViewById(R.id.changePasswordButton);
        changePasswordButton.setOnClickListener(v -> changePassword());

        // Listener para alternar modo oscuro/claro
        darkModeSwitch.setOnCheckedChangeListener((compoundButton, checked) -> toggleDarkMode(checked));

        profileViewModel = new ViewModelProvider(this).get(ProfileViewModel.class);

        return view;
    }

    private void changePassword() {
        String currentPass = currentPasswordEditText.getText().toString();
        String newPass = newPasswordEditText.getText().toString();

        //pasar los valores a viewmodel
        profileViewModel.setChangePasswordDetails(newPass , currentPass);

        // Observamos el LiveData para actualizar la UI con el estado del registro
        profileViewModel.getChangePasswordStatus().observe((LifecycleOwner) requireContext(), status -> {
            //esto es un control para que no aparezcan dos toast
            if (!status.equals("hola")){
                    Toast.makeText(getContext(), status, Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void toggleDarkMode(boolean enableDarkMode) {
        // Guardamos la preferencia
        SharedPreferences prefs = requireActivity().getSharedPreferences("AppConfig", Context.MODE_PRIVATE);
        prefs.edit().putBoolean("darkMode", enableDarkMode).apply();

        // Aplicamos el tema
        if (enableDarkMode) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }

        // Recreamos la activity para que se aplique el cambio
        requireActivity().recreate();
    }
}