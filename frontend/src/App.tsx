import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import DataCenters from './pages/DataCenters';
import Assets from './pages/Assets';
import Lifecycle from './pages/Lifecycle';
import Capacity from './pages/Capacity';
import Changes from './pages/Changes';
import Licenses from './pages/Licenses';
import { AuthProvider } from './lib/auth';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <div className="flex h-screen bg-gray-950 text-gray-100 overflow-hidden">
          <Sidebar />
          <main className="flex-1 overflow-y-auto bg-gray-950 p-6">
            <Routes>
              <Route path="/" element={<Navigate to="/dashboard" replace />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/datacenters" element={<DataCenters />} />
              <Route path="/assets" element={<Assets />} />
              <Route path="/lifecycle" element={<Lifecycle />} />
              <Route path="/capacity" element={<Capacity />} />
              <Route path="/changes" element={<Changes />} />
              <Route path="/licenses" element={<Licenses />} />
            </Routes>
          </main>
        </div>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
