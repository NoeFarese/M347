# Wie werden von Kubernetes Container ausgeführt und verwaltet

![BBZW Logo](https://github.com/IneichenBBZW/M347_Bilder/blob/main/bbzw_logo.png?raw=true)

## Pod

Kubernetes hüllt den Container in eine andere virtualisierte Umgebung ein, welche Pod bezeichnet wird.

Ein Pod ist eine Recheneinheit, die auf einem einzelnen Knoten im Cluster ausgeführt wird.

![Sie verwalten Pods und Pods verwalten Container.](https://github.com/IneichenBBZW/M347_Bilder/blob/main/Pods.png?raw=true)

## Pod über Kubernetes-Kommandos ausführen

Einen Pod mit einem einzigen Container betreiben.

```Powershell
kubectl run hello-kubernetes --image=mainho/hello-kubernetes --restart=Always
```

Alle Pods des Clusters auflisten.

```Powershell
kubectl get pods
```

Detaillierte Informationen über den Pod anzeigen.

```Powershell
kubectl describe pod hello-kubernetes
```

[Ausführen eines Pods mit kubectl](https://github.com/IneichenBBZW/M347_Auswertung_b/blob/main/b_Auswertung1.png?raw=true)

## Informationen zum Pod anfordern

Die grundlegenden Informationen über den Pod abrufen.

```Powershell
kubectl get pod hello-kubernetes
```

Benutzerdefinierte Spalten in der Ausgabe angeben, Netzwerkdetails auswählen.

```Powershell
kubectl get pod hello-kubernetes --output custom-columns=NAME:metadata.name,NODE_IP:status.hostIP,POD_IP:status.podIP
```

Eine JSONPath-Abfrage in der Ausgabe angeben, Auswahl der ID des ersten Containers im Pod.

```Powershell
kubectl get pod hello-kubernetes -o jsonpath='{.status.containerStatuses[0].containerID}'
```

[Optionen zur Ausgabe für Pods](https://github.com/IneichenBBZW/M347_Auswertung_b/blob/main/b_Auswertung2.png?raw=true)


## Kubernetes-Knoten hält seine Pod-Container am laufen

Den Container des Pods finden.

```Powershell
docker container ls -q --filter label=io.kubernetes.container.name=hello-kubernetes
```

Löschen Sie nun diesen Container!

```Powershell
docker container rm -f $(docker container ls -q --filter label=io.kubernetes.container.name=hello-kubernetes)
```

Den Status des Pods prüfen.

```Powershell
kubectl get pod hello-kubernetes
```

Den Container wiederfinden.

```Powershell
docker container ls -q --filter label=io.kubernetes.container.name=hello-kubernetes
```

[Kubernetes stellt sicher, dass Pods alle benötigten Container verfügen.](https://github.com/IneichenBBZW/M347_Auswertung_b/blob/main/b_Auswertung3.png?raw=true)

## In den Pod schauen

Eine Portweiterleitung an den Host machen. Container: 80 --> Host: 8080

```Powershell
kubectl port-forward pod/hello-kubernetes 8080:80
```

Rufen Sie jetzt [http://localhost:8080](http://localhost:8080) auf.

Wenn Sie fertig sind, drücken Sie ctrl-c, um die Weiterleitung zu beenden.

[Mit kubectl Portweiterleitung einrichten.](https://github.com/IneichenBBZW/M347_Auswertung_b/blob/main/b_Auswertung4.png?raw=true)