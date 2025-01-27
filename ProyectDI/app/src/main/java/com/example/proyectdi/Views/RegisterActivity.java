package com.example.proyectdi.Views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;

import com.example.proyectdi.R;
import com.example.proyectdi.ViewModels.RegisterViewModel;
import com.example.proyectdi.databinding.ActivityRegisterBinding;

public class RegisterActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //mostrar activity
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        ActivityRegisterBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_register);
        
        // Crear una instancia del ViewModel
        RegisterViewModel registerViewModel = new ViewModelProvider(this).get(RegisterViewModel.class);

        //inicializar boton
        Button button = binding.registerButton;
        //cuando el boton sea pulsado ir a registerUser
        button.setOnClickListener(v ->{
            //inicializar valores
            String fullName = binding.fullNameEditText.getText().toString();
            String email = binding.emailEditText.getText().toString();
            String password = binding.passwordEditText.getText().toString();
            String passwordConfirm = binding.passwordConfirmEditText.getText().toString();
            String phone = binding.phoneEditText.getText().toString();
            String address = binding.addressEditText.getText().toString();

            //pasar los valores a viewmodel
            registerViewModel.setRegistrationDetails(fullName, email, password, passwordConfirm, phone, address);
            // Observamos el LiveData para actualizar la UI con el estado del registro
            registerViewModel.getRegistrationStatus().observe(this, status -> {
                // Actualizamos el estado en la UI
                Toast.makeText(this, status, Toast.LENGTH_SHORT).show();

                // Si el registro fue exitoso, podemos hacer algo más (como navegar a otra actividad)
                if (status.equals("Registro exitoso.")) {
                    // Redirigir a la pantalla de login
                    Intent intent = new Intent(RegisterActivity.this, LoginActivity.class);
                    startActivity(intent);
                    finish(); // Cerramos la actividad actual
                }
            });
        });
    }
}


