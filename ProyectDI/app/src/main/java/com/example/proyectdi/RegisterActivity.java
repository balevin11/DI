package com.example.proyectdi;

import android.content.Context;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import com.google.firebase.auth.FirebaseAuth;

public class RegisterActivity extends AppCompatActivity {
    private EditText editTextFullName, editTextEmail, editTextPassword, editTextPassworConfirm, editTextPhone, editTextAddress;
    private FirebaseAuth mAuth;
    private Button button;
    private final Context context = this;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_register);
        editTextFullName = findViewById(R.id.fullNameEditText);
        editTextEmail = findViewById(R.id.emailEditText);
        editTextPassword = findViewById(R.id.passwordEditText);
        editTextPassworConfirm = findViewById(R.id.passwordConfirmEditText);
        editTextPhone = findViewById(R.id.phoneEditText);
        editTextAddress = findViewById(R.id.addressEditText);
        button = findViewById(R.id.registerButton);
        mAuth = FirebaseAuth.getInstance();
        if (editTextFullName.length() <= 0 || editTextPassword.length() <= 0 || editTextPassworConfirm.length() <= 0 || editTextPhone.length() <= 0 || editTextAddress.length() <= 0) {
            Toast.makeText(context, "All parameters must be covered.", Toast.LENGTH_SHORT).show();
        }
        if (!editTextPassword.equals(editTextPassworConfirm)) {
            Toast.makeText(context, "Password confirmation is wrong", Toast.LENGTH_SHORT).show();
        }
        button.setOnClickListener(v -> registerUser());
    }

    private void registerUser(){
        mAuth.createUserWithEmailAndPassword(editTextEmail.getText().toString(), editTextPassword.getText().toString()).addOnCompleteListener(this, task -> {
            if (task.isSuccessful()) {
                Toast.makeText(context, "Usuario registrado correctamente.", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(context, "Error en el registro: " + task.getException().getMessage(), Toast.LENGTH_SHORT).show();
            }
        });
    }
}