package com.example.proyectdi.Models;

public class Games {
    private String url, nombre, descripcion, id;

    public Games() {
    }

    public Games(String url, String nombre, String descripcion, String id) {
        this.url = url;
        this.nombre = nombre;
        this.descripcion = descripcion;
    }
    public String getUrl() {
        return url;
    }

    public String getNombre() {
        return nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }
    public String getId() {
        return id;
    }

}
