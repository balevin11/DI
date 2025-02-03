package com.example.proyectdi.views;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.lifecycle.ViewModelProvider;
import com.example.proyectdi.R;
import com.example.proyectdi.viewmodels.LoginViewModel;
import com.example.proyectdi.databinding.ActivityLoginBinding;

public class LoginActivity extends AppCompatActivity {
    //inicializar variables
    private final Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //mostrar activity
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        ActivityLoginBinding binding = DataBindingUtil.setContentView(this, R.layout.activity_login);

        // Crear una instancia del ViewModel
        LoginViewModel loginViewModel = new ViewModelProvider(this).get(LoginViewModel.class);

        //inicializar botones
        Button loginButton = binding.loginButton;
        Button registerButton = binding.registerButton;

        //cuando se pulse boton login ir a metodo login
        loginButton.setOnClickListener(v-> {

            //dar valores a las variables
            String email = binding.emailEditText.getText().toString();
            String password = binding.passwordEditText.getText().toString();

            //pasar los valores a viewmodel
            loginViewModel.setLoginDetails(email, password);

            // Observamos el LiveData para actualizar la UI con el estado del registro
            loginViewModel.getLoginStatus().observe(this, status -> {
                // Actualizamos el estado en la UI
                Toast.makeText(this, status, Toast.LENGTH_SHORT).show();

                // Si el registro fue exitoso, podemos hacer algo más (como navegar a otra actividad)
                if (status.equals("Sesión iniciada.")) {
                    //abrir activity dashboard
                    Intent intent = new Intent(context, DashboardActivity.class);
                    startActivity(intent);
                }
            });

        });

        //cuando se pulse boton register ir a metodo register
        registerButton.setOnClickListener(v->register());
    }

    private void register(){
        //abrir activity register
        Intent intent = new Intent(context, RegisterActivity.class);
        startActivity(intent);
    }
}