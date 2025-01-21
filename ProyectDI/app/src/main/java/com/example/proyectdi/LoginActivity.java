package com.example.proyectdi;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;

public class LoginActivity extends AppCompatActivity {
    //inicializar variables
    private Button registerButton,loginButton;
    private EditText editTextEmail, editTextPassword;
    private final Context context = this;
    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        //mostrar activity
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_login);

        //dar valores a las variables
        editTextEmail = findViewById(R.id.emailEditText);
        editTextPassword  = findViewById(R.id.passwordEditText);
        registerButton = findViewById(R.id.registerButton);
        loginButton = findViewById(R.id.loginButton);
        mAuth = FirebaseAuth.getInstance();

        //cuando se pulse boton login ir a metodo login
        loginButton.setOnClickListener(v->login());
        //cuando se pulse boton register ir a metodo register
        registerButton.setOnClickListener(v->register());
    }
    private void register(){
        //abrir activity register
        Intent intent = new Intent(context, RegisterActivity.class);
        startActivity(intent);
    }
    private void login(){
        //iniciar sesion en firebase con email y contraseña, toast de error y éxito
        mAuth.signInWithEmailAndPassword(editTextEmail.getText().toString(), editTextPassword.getText().toString())
                .addOnCompleteListener(this, task -> {
                    if (task.isSuccessful()) {
                        Toast.makeText(context, "Inicio de sesión exitoso.", Toast.LENGTH_SHORT).show();
                        //abrir activity dashboard
                        Intent intent = new Intent(context, Dashboard_Activity.class);
                        startActivity(intent);
                    } else {
                        Toast.makeText(context, "Error en autenticación.", Toast.LENGTH_SHORT).show();
                    }
                });
    }
}