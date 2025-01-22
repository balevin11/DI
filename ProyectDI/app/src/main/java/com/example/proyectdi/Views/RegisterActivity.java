package com.example.proyectdi.Views;



import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import com.example.proyectdi.R;
import com.example.proyectdi.ViewModels.RegisterViewModel;
import com.google.firebase.auth.FirebaseAuth;

public class RegisterActivity extends AppCompatActivity {
    //inicializar variables
    private EditText editTextFullName, editTextEmail, editTextPassword, editTextPasswordConfirm, editTextPhone, editTextAddress;
    private FirebaseAuth mAuth;
    private final Context context = this;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //mostrar activity
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_register);

        //dar valores a las variables
        editTextFullName = findViewById(R.id.fullNameEditText);
        editTextEmail = findViewById(R.id.emailEditText);
        editTextPassword = findViewById(R.id.passwordEditText);
        editTextPasswordConfirm = findViewById(R.id.passwordConfirmEditText);
        editTextPhone = findViewById(R.id.phoneEditText);
        editTextAddress = findViewById(R.id.addressEditText);
        Button button = findViewById(R.id.registerButton);

        //cuando el boton sea pulsado ir a registerUser
        button.setOnClickListener(v -> registerUser());
    }

    private void registerUser(){
        //crear un registerViewModel para obtener los usuarios
        RegisterViewModel registerViewModel = new ViewModelProvider(this).get(RegisterViewModel.class);
        registerViewModel.getRegistrationStatus().observe(this, new observer <String>(){
            pass;
        });

    }
}

