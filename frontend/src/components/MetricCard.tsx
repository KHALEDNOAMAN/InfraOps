import React from 'react';

export default function MetricCard({ icon: Icon, label, value, trend }: any) {
  const isPositive = trend > 0;
  return (
    <div className="bg-gray-900 p-6 rounded-xl border border-gray-800 flex items-center justify-between">
      <div>
        <p className="text-sm text-gray-400 mb-1">{label}</p>
        <h3 className="text-2xl font-bold text-gray-100">{value}</h3>
      </div>
      <div className="flex flex-col items-end">
        <div className="p-3 bg-gray-800 rounded-lg text-cyan-400 mb-2">
          <Icon size={24} />
        </div>
        {trend !== undefined && (
          <span className={`text-sm ${isPositive ? 'text-green-400' : 'text-red-400'}`}>
            {isPositive ? '+' : ''}{trend}%
          </span>
        )}
      </div>
    </div>
  );
}
