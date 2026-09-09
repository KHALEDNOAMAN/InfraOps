import React from 'react';

const columns = ['Draft', 'Pending', 'Approved', 'In Progress', 'Completed'];
const tickets = [
  { id: 'CR-101', title: 'Upgrade DB Cluster', status: 'Pending', risk: 'High' },
  { id: 'CR-102', title: 'Patch OS on Web Nodes', status: 'Approved', risk: 'Medium' },
  { id: 'CR-103', title: 'Replace Switch SW-01', status: 'In Progress', risk: 'High' },
];

export default function Changes() {
  const getRiskColor = (risk: string) => {
    if (risk === 'High') return 'bg-red-500/20 text-red-400';
    if (risk === 'Medium') return 'bg-yellow-500/20 text-yellow-400';
    return 'bg-green-500/20 text-green-400';
  };

  return (
    <div className="space-y-6 h-full flex flex-col">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Change Management</h1>
        <button className="bg-cyan-600 hover:bg-cyan-700 px-4 py-2 rounded-lg font-medium">Create CR</button>
      </div>

      <div className="flex gap-4 flex-1 overflow-x-auto pb-4">
        {columns.map(col => (
          <div key={col} className="w-80 flex-shrink-0 bg-gray-900/50 rounded-xl p-4 flex flex-col border border-gray-800">
            <h3 className="font-bold text-gray-400 mb-4">{col}</h3>
            <div className="space-y-3 flex-1">
              {tickets.filter(t => t.status === col).map(t => (
                <div key={t.id} className="bg-gray-800 p-4 rounded-lg border border-gray-700 cursor-pointer hover:border-gray-500 transition-colors">
                  <div className="flex justify-between items-start mb-2">
                    <span className="text-xs text-gray-400 font-mono">{t.id}</span>
                    <span className={`text-[10px] px-2 py-0.5 rounded-full ${getRiskColor(t.risk)}`}>{t.risk}</span>
                  </div>
                  <h4 className="font-medium text-sm">{t.title}</h4>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
