package com.example.catalogactivity;



import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

import androidx.fragment.app.Fragment;
import androidx.navigation.NavController;
import androidx.navigation.fragment.NavHostFragment;


public class CatalogFragment extends Fragment {


    public CatalogFragment() {
        // Required empty public constructor
    }

    public static CatalogFragment newInstance() {
        CatalogFragment fragment = new CatalogFragment();

        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


    }

    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_catalog,container,false);
        Button button = view.findViewById(R.id.detail);
        button.setOnClickListener(v -> {
            NavController navcontroller = NavHostFragment.findNavController(this);
            navcontroller.navigate(R.id.action_catalog_to_details);
        });
        return view;
    }
}