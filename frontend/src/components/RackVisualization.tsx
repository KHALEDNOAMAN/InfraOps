import React from 'react';

export default function RackVisualization({ units = 42, assets = [] }: any) {
  const uArray = Array.from({ length: units }, (_, i) => units - i);
  
  return (
    <div className="w-64 border-4 border-gray-700 bg-gray-900 p-2 rounded-t-lg">
      <div className="text-center font-bold mb-4 text-gray-400">RACK 1</div>
      <div className="flex flex-col gap-1">
        {uArray.map(u => {
          const asset = assets.find((a: any) => a.u === u);
          return (
            <div key={u} className="flex items-center text-xs">
              <span className="w-6 text-gray-500">{u}U</span>
              <div 
                className={`flex-1 h-4 rounded-sm border border-gray-800 ${
                  asset 
                    ? asset.type === 'server' ? 'bg-cyan-900' : 'bg-purple-900' 
                    : 'bg-gray-800'
                }`}
                title={asset?.name || 'Empty'}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
}
