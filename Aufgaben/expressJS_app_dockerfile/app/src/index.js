"use strict";
import express from "express";

const app = express();
const PORT = 8080;

app.get("/", (req, res) => {
  res.send("<h1>Express JS Applikation läuft mit Docker</h1>");
});

app.listen(PORT, () => {
  console.log(`Server läuft unter http://localhost:${PORT}`);
});
