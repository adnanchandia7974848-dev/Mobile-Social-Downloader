import os
import sys

# Ensure current directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Set desktop window dimensions for mobile emulation
from kivy.config import Config
Config.set('graphics', 'width', '380')
Config.set('graphics', 'height', '720')
Config.set('graphics', 'resizable', '1')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition, NoTransition
from kivy.core.window import Window

from storage.settings import AppSettings
from storage.download_history import DownloadHistory
from services.download_manager import DownloadManager

from ui.dashboard import DashboardScreen
from ui.platform_page import PlatformDownloadScreen
from ui.downloads_page import DownloadsScreen
from ui.settings_page import SettingsScreen

class SocialMediaDownloaderApp(App):
    def build(self):
        self.title = "A Social Downloader"

        # Determine user data directory for storage
        user_data_path = self.user_data_dir
        os.makedirs(user_data_path, exist_ok=True)

        self.settings = AppSettings(storage_dir=user_data_path)
        self.history = DownloadHistory(storage_dir=user_data_path)
        self.download_manager = DownloadManager(history=self.history, settings=self.settings)

        self.sm = ScreenManager(transition=NoTransition())

        # Dashboard screen
        self.dashboard_screen = DashboardScreen()
        self.sm.add_widget(self.dashboard_screen)

        # Platform Screens
        self.youtube_screen = PlatformDownloadScreen("YouTube", self.download_manager, self.history, name="youtube")
        self.facebook_screen = PlatformDownloadScreen("Facebook", self.download_manager, self.history, name="facebook")
        self.instagram_screen = PlatformDownloadScreen("Instagram", self.download_manager, self.history, name="instagram")
        self.twitter_screen = PlatformDownloadScreen("Twitter / X", self.download_manager, self.history, name="twitter")

        self.sm.add_widget(self.youtube_screen)
        self.sm.add_widget(self.facebook_screen)
        self.sm.add_widget(self.instagram_screen)
        self.sm.add_widget(self.twitter_screen)

        # Downloads & Settings Screens
        self.downloads_screen = DownloadsScreen(self.download_manager, self.history, name="downloads")
        self.settings_screen = SettingsScreen(self.settings, self.history, name="settings")

        self.sm.add_widget(self.downloads_screen)
        self.sm.add_widget(self.settings_screen)

        # Bind hardware back button (Android)
        Window.bind(on_keyboard=self.on_hardware_back)

        # Request Android permissions if on Android
        from kivy.utils import platform
        if platform == 'android':
            try:
                from android.permissions import request_permissions, Permission
                request_permissions([
                    Permission.INTERNET,
                    Permission.READ_EXTERNAL_STORAGE,
                    Permission.WRITE_EXTERNAL_STORAGE
                ])
            except Exception as pe:
                print(f"[App] Android permission request error: {pe}")

        return self.sm

    def on_hardware_back(self, window, key, *args):
        # 27 is the escape / back key code
        if key == 27:
            if self.sm.current != 'dashboard':
                self.sm.current = 'dashboard'
                return True
        return False

if __name__ == '__main__':
    SocialMediaDownloaderApp().run()
