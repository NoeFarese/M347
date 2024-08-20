# Pod mit Controllern betreiben

![BBZW Logo](https://github.com/IneichenBBZW/M347_Bilder/blob/main/bbzw_logo.png?raw=true)

Ein Controller ist eine Kubernetes-Ressource, die andere Ressourcen verwaltet.

Kubernetes hat viele Controller, aber der wichtigste für die Verwaltung von Pods ist das Deployment.

![Deployment-Controller verwalten Pods und Pods verwalten Container.](https://github.com/IneichenBBZW/M347_Bilder/blob/main/Deployment-Controller.png?raw=true)

Erstellen Sie ein Deployment mit dem Namen "hello-kubernetes-2" auf der die gleiche Webanwendung läuft.

```Powershell
kubectl create deployment hello-kubernetes-2 --image=mainho/hello-kubernetes
```

Alle Pods auflisten.

```Powershell
kubectl get pods
```

[Erstellen einer Controller-Ressource, die ihre eigenen Ressourcen erstellt - Deployments erstellen Pods](https://github.com/IneichenBBZW/M347_Auswertung_c/blob/main/c_Auswertung1.png?raw=true)

## Kubernetes Ressourcen können Labels zugewiesen werden

Die Label anzeigen, die das Deployment dem Pod hinzufügt.

```Powershell
 kubectl get deploy hello-kubernetes-2 -o jsonpath='{.spec.template.metadata.labels}'
```

Die Pods auflisten, die das entsprechende Label haben.

```Powershell
kubectl get pods -l app=hello-kubernetes-2
```

[Deployments fügen beim Erstellen von Pods Labels hinzu, die sie als Filter verwenden können.](https://github.com/IneichenBBZW/M347_Auswertung_c/blob/main/c_Auswertung2.png?raw=true)

![Controller identifizieren die von ihnen verwalteten Ressourcen mithilfe con Labels](https://github.com/IneichenBBZW/M347_Bilder/blob/main/Controller_Ressourcen_Label.png?raw=true)

## Das Deployment hat keine direkte Beziehung zum vom ihm erstellten Pod

Alle Pods auflisten, mit Angabe des Pod-Namens und den Bezeichnungen.

```Powershell
 kubectl get pods -o custom-columns=NAME:metadata.name,LABELS:metadata.labels
```

Die Bezeichnung "app" für den Pod des Deployments mit einem anderen Wert aktualisieren.

```Powershell
kubectl label pods -l app=hello-kubernetes-2 --overwrite app=hello-kubernetes-x
```

Pods wieder anzeigen.

```Powershell
kubectl get pods -o custom-columns=NAME:metadata.name,LABELS:metadata.labels
```

[Wenn Sie das Label des Pods ändern, wird dieser der Kontrolle durch das Deployment entzogen.](https://github.com/IneichenBBZW/M347_Auswertung_c/blob/main/c_Auswertung3.png?raw=true)

## Ein Pod wieder unter die Kontrolle des Deployment bringen

Alle Pods mit einem Label namens "app" auflisten und den Pod-Namen und Label anzeigen.

```Powershell
kubectl get pods -l app -o custom-columns=NAME:metadata.name,LABELS:metadata.labels
```

Das Label "app" für den nicht verwalteten Pod aktualisieren.

```Powershell
kubectl label pods -l app=hello-kubernetes-x --overwrite app=hello-kubernetes-2
```

Pods wieder anzeigen.

```Powershell
kubectl get pods -l app -o custom-columns=NAME:metadata.name,LABELS:metadata.labels
```

[Die erneute Änderung des Labels bringen den Pod wieder unter Kontrolle des Deployments.](https://github.com/IneichenBBZW/M347_Auswertung_c/blob/main/c_Auswertung4.png?raw=true)

## Portweiterleitung auf Ebene der Deployment-Ressource konfigurieren

Führen Sie eine Portweiterleitung von Ihrem lokalen Rechner zum Deployment.

```Powershell
kubectl port-forward deploy/hello-kubernetes-2 8080:80
```

Öffnen Sie im Browser [http://localhost:8080](http://localhost:8080)

Wenn Sie fertig sind, beenden Sie die Weiterleitung mit ctrl-c.

[Pods und Deployments sind Schichten über den Containern, aber die Anwendung läuft immer noch in einem Container.](https://github.com/IneichenBBZW/M347_Auswertung_c/blob/main/c_Auswertung5.png?raw=true)

