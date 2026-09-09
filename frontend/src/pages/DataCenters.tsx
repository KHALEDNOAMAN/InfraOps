import React from 'react';
import RackVisualization from '../components/RackVisualization';

export default function DataCenters() {
  const mockAssets = [
    { u: 42, type: 'switch', name: 'Core Switch' },
    { u: 40, type: 'server', name: 'DB Node 1' },
    { u: 38, type: 'server', name: 'App Node 1' },
  ];

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Data Centers</h1>
        <button className="bg-cyan-600 hover:bg-cyan-700 text-white px-4 py-2 rounded-lg font-medium transition-colors">
          Add Data Center
        </button>
      </div>

      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        <div className="xl:col-span-1 space-y-4">
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 cursor-pointer border-cyan-500/50">
            <h3 className="font-bold text-lg">NYC-1 (Primary)</h3>
            <p className="text-gray-400 text-sm mb-4">New York, USA</p>
            <div className="flex justify-between text-sm">
              <span>12 Racks</span>
              <span className="text-green-400">Healthy</span>
            </div>
          </div>
          <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 cursor-pointer">
            <h3 className="font-bold text-lg">LON-1 (DR)</h3>
            <p className="text-gray-400 text-sm mb-4">London, UK</p>
            <div className="flex justify-between text-sm">
              <span>8 Racks</span>
              <span className="text-green-400">Healthy</span>
            </div>
          </div>
        </div>

        <div className="xl:col-span-2 bg-gray-900 p-6 rounded-xl border border-gray-800 min-h-[600px] flex items-center justify-center">
          <div className="flex gap-12">
            <RackVisualization units={42} assets={mockAssets} />
            <RackVisualization units={42} assets={[]} />
            <RackVisualization units={42} assets={[]} />
          </div>
        </div>
      </div>
    </div>
  );
}
