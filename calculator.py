import tkinter as tk
from tkinter import messagebox

# Funktion zur Umrechnung von Hexadezimal in Binär
def hex_to_bin():
    hex_value = entry.get().strip()
    try:
        # Hexadezimal in Ganzzahl umwandeln, dann in Binär konvertieren und "0b"-Präfix entfernen
        binary_value = bin(int(hex_value, 16))[2:]
        result_label.config(text=f"Binär: {binary_value}")
    except ValueError:
        # Fehlermeldung anzeigen, wenn die Eingabe keine gültige Hexadezimalzahl ist
        messagebox.showerror("Fehler", "Bitte eine gültige hexadezimale Zahl eingeben.")

# GUI initialisieren
root = tk.Tk()
root.title("Hex zu Binär Rechner")
root.geometry("300x150")

# Eingabefeld und Label
tk.Label(root, text="Hexadezimal eingeben:").pack(pady=5)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# Button zur Umrechnung
convert_button = tk.Button(root, text="In Binär umwandeln", command=hex_to_bin)
convert_button.pack(pady=5)

# Ergebnis-Label
result_label = tk.Label(root, text="Binär: ")
result_label.pack(pady=10)

# GUI ausführen
root.mainloop()
