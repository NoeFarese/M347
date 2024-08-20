# Kubernetes Einführung

![BBZW Logo](https://github.com/IneichenBBZW/M347_Bilder/blob/main/bbzw_logo.png?raw=true)

Kubernetes ist eine Plattform für den Betrieb von Containern. Sie kümmert sich um den Start Ihrer containerisierten Anwendungen, das Ausrollen von Updates, die Aufrechterhaltung von Service-Levels, die bedarfsgerechte Skalierung, die Sicherung des Zugriffs und vieles mehr.

Die beiden Kernkonzepte von Kubernetes sind die API, über die Sie Ihre Anwendungen definieren, und der Cluster, auf dem Ihre Anwendungen ausgeführt werden. Ein Cluster ist ein Satz einzelner Server, die alle mit einer Container-Laufzeitumgebung wie Docker konfiguriert und dann mit Kubernetes zu einer einzigen logischen Einheit verbunden wurden.

![Ein Kubernetes-Cluster ist ein Bündel von Servern, die Container ausführen können und zu einer Gruppe zusammengefasst sind.](https://github.com/IneichenBBZW/M347_Bilder/blob/main/Kubernetes-Cluster.png?raw=true)

Der Kubernetes-Cluster ist dazu da, Ihre Anwendungen auszuführen. Sie definieren Ihre Anwendungen in YAML-Dateien und senden diese Dateien an die Kubernetes-API. Kubernetes prüft die in der YAML-Datei enthaltenen Anforderungen und vergleicht sie mit dem, was bereits im Cluster ausgeführt wird. Es nimmt alle erforderlichen Änderungen vor, um den gewünschten Zustand zu erreichen, z.B. das Aktualisieren einer Konfiguration, das Entfernen von Containern oder das Erstellen neuer Container.

Wenn eine Komponente aufgrund einer hohen Last unter Stress steht, kann Kubernetes zusätzliche Kopien der Komponente in neuen Containern starten. Wenn Sie die Arbeit in Ihre Docker-Images und Kubernetes-YAML-Dateien stecken, erhalten Sie eine selbstheilende Anwendung, die auf jedem Kubernetes-Cluster auf die gleiche Weise läuft.

![Anwendungen in einem Kubernetes-Cluster bereitstellen](https://github.com/IneichenBBZW/M347_Bilder/blob/main/Anwendungen-bereitstellen.png?raw=true)

Kubernetes verwaltet mehr als nur Container, was es zu einer vollständigen Anwendungsplattform macht. Der Cluster verfügt über eine verteilte Datenbank, in der Sie sowohl Konfigurationsdateien für Ihre Anwendungen als auch Keys wie API-Keys und Verbindungsdaten speichern können. Kubernetes stellt diese nahtlos für Ihre Container bereit, sodass Sie in jeder Umgebung dieselben Container-Images verwenden und die korrekte Konfiguration aus dem Cluster anwenden können. Kubernetes stellt auch Speicher zur Verfügung, so dass Ihre Anwendungen Daten ausserhalb von Containern aufbewahren können, wodurch Sie eine hohe Verfügbarkeit für zustandsabhängige Anwendungen erhalten. Kubernetes verwaltet auch den in dem Cluster eingehenden Netzwerkverkehr, indem es ihn zur Verarbeitung an die richtigen Container weiterleitet.

![Der Kubernetes Cluster bietet auch andere Ressourcen](https://github.com/IneichenBBZW/M347_Bilder/blob/main/Kubernetes-verwaltet-Resourcen.png?raw=true)

## Komponenten der Kubernetes-Ressourcen

![Die grundlegensten Kubernetes Ressourcen](https://github.com/IneichenBBZW/M347_Bilder/blob/main/Kubernetes-Ressourcen.png?raw=true)