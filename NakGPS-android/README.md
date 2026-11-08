# NakGPS – APK para Android

App de Android (Capacitor) con la página de NakGPS adentro. El APK se compila solo en la nube; no necesitas instalar Android Studio.

## Opción A: crear el APK con GitHub (sin instalar nada)

1. Crea una cuenta gratis en https://github.com y un repositorio nuevo (por ejemplo `nakgps`).
2. Sube TODO el contenido de esta carpeta al repositorio. Importante: incluye la carpeta oculta `.github`.
   - Desde la web: botón **Add file → Upload files**, arrastra los archivos y carpetas (si tu computadora no deja ver `.github`, usa Git: `git init`, `git add .`, `git commit`, `git push`).
3. Entra a la pestaña **Actions** del repositorio. Verás "Crear APK de NakGPS" corriendo (tarda unos 5 a 8 minutos). Si no arranca solo, pulsa **Run workflow**.
4. Cuando termine, abre esa ejecución, baja hasta **Artifacts** y descarga **NakGPS-apk**. Dentro viene `app-debug.apk`.
5. Pásalo al teléfono (WhatsApp, cable o Drive), ábrelo y acepta "Instalar apps de origen desconocido" cuando Android lo pida.

## Opción B: compilar en tu computadora

Necesitas Node.js 20+, Java 17 y Android Studio.

```
npm install
npx cap add android
pip install pillow && python3 tools/prepare_android.py
npx cap sync android
cd android && ./gradlew assembleDebug
```

El APK queda en `android/app/build/outputs/apk/debug/app-debug.apk`.

## Cambios frecuentes

- **Actualizar la página:** reemplaza `www/index.html` por la versión nueva y vuelve a subir (Opción A) o ejecuta `npx cap sync android` y compila (Opción B).
- **Nombre o identificador:** edita `appName` y `appId` en `capacitor.config.json` (el `appId` no se puede cambiar después de publicar en Google Play).
- **Ubicación:** el APK pide permiso de ubicación la primera vez. La calibración y los ajustes se guardan en el teléfono.

## Para Google Play

Este APK es de prueba (firma de depuración). Para publicarlo en Google Play hay que generar un paquete AAB firmado con tu propia llave (`./gradlew bundleRelease`) y tener cuenta de desarrollador.
