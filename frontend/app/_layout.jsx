import { StatusBar } from 'expo-status-bar';
import { Stack } from "expo-router";
import React from 'react';

export default function RootLayout() {
    return (
        <React.Fragment>
        <StatusBar style="auto" />
            <Stack>
                {/* Home Screen */}
                <Stack.Screen name="index" options={{ title: "Home" }} />

                {/* Test Screen */}
                <Stack.Screen name="test" options={{ title: "Test Screen", headerShown: false}} />

            </Stack>
        </React.Fragment>
    );
}