import React from 'react';

export default function Lifecycle() {
  const stages = ['Ordered', 'Received', 'Deployed', 'Maintenance', 'Retired', 'Disposed'];
  
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Lifecycle Management</h1>
      
      <div className="flex w-full items-center justify-between p-6 bg-gray-900 rounded-xl border border-gray-800">
        {stages.map((stage, i) => (
          <React.Fragment key={stage}>
            <div className="flex flex-col items-center">
              <div className="w-12 h-12 rounded-full bg-cyan-900/50 border border-cyan-500/50 flex items-center justify-center font-bold text-cyan-400 mb-2">
                {Math.floor(Math.random() * 50)}
              </div>
              <span className="text-sm font-medium">{stage}</span>
            </div>
            {i < stages.length - 1 && <div className="h-[2px] flex-1 bg-gray-800 mx-4 mt-[-20px]"></div>}
          </React.Fragment>
        ))}
      </div>

      <div className="bg-gray-900 p-6 rounded-xl border border-gray-800">
        <h2 className="text-lg font-medium mb-4">Recent Events</h2>
        <div className="space-y-4">
          {[1,2,3].map(i => (
            <div key={i} className="flex gap-4 border-l-2 border-cyan-500 pl-4 py-2">
              <div className="text-sm text-gray-400 min-w-[100px]">2 hours ago</div>
              <div>
                <p className="font-medium text-gray-200">Asset SRV-04{i} moved to Deployed</p>
                <p className="text-sm text-gray-500">By Admin User</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
