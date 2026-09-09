import React from 'react';
import StatusBadge from '../components/StatusBadge';
import { Search, Filter } from 'lucide-react';

const mockAssets = [
  { id: 1, tag: 'SRV-001', host: 'web-prod-1', type: 'Server', ip: '10.0.1.10', rack: 'NYC-1-A1', status: 'active' },
  { id: 2, tag: 'SRV-002', host: 'db-prod-1', type: 'Server', ip: '10.0.1.11', rack: 'NYC-1-A1', status: 'active' },
  { id: 3, tag: 'SW-001', host: 'core-sw-1', type: 'Switch', ip: '10.0.0.1', rack: 'NYC-1-A1', status: 'maintenance' },
];

export default function Assets() {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Assets</h1>
        <button className="bg-cyan-600 hover:bg-cyan-700 px-4 py-2 rounded-lg font-medium">Add Asset</button>
      </div>

      <div className="flex gap-4 mb-6">
        <div className="relative flex-1 max-w-md">
          <Search className="absolute left-3 top-2.5 text-gray-500" size={20} />
          <input type="text" placeholder="Search assets..." className="w-full bg-gray-900 border border-gray-800 rounded-lg pl-10 pr-4 py-2 focus:outline-none focus:border-cyan-500" />
        </div>
        <button className="flex items-center gap-2 px-4 py-2 bg-gray-900 border border-gray-800 rounded-lg text-gray-300">
          <Filter size={20} /> Filters
        </button>
      </div>

      <div className="bg-gray-900 rounded-xl border border-gray-800 overflow-hidden">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="bg-gray-800/50 text-gray-400 text-sm border-b border-gray-800">
              <th className="p-4 font-medium">Asset Tag</th>
              <th className="p-4 font-medium">Hostname</th>
              <th className="p-4 font-medium">Type</th>
              <th className="p-4 font-medium">IP Address</th>
              <th className="p-4 font-medium">Location</th>
              <th className="p-4 font-medium">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-800">
            {mockAssets.map(asset => (
              <tr key={asset.id} className="hover:bg-gray-800/30 transition-colors cursor-pointer">
                <td className="p-4 font-medium">{asset.tag}</td>
                <td className="p-4">{asset.host}</td>
                <td className="p-4">{asset.type}</td>
                <td className="p-4 text-gray-400">{asset.ip}</td>
                <td className="p-4">{asset.rack}</td>
                <td className="p-4"><StatusBadge status={asset.status} /></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
